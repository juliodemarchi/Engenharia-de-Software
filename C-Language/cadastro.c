#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int id;
    char nome[50];
    char email[50];
} Usuario;

// Protótipos das funções
void criar_usuario();
void listar_usuarios();
void atualizar_usuario();
void deletar_usuario();

const char* DB_FILE = "banco.dat";

int main() {
    int opcao;

    do {
        printf("\n--- SISTEMA DE BANCO DE DADOS EM C ---\n");
        printf("1. Criar Usuário\n");
        printf("2. Listar Usuários\n");
        printf("3. Atualizar Usuário\n");
        printf("4. Deletar Usuário\n");
        printf("0. Sair\n");
        printf("Escolha: ");
        scanf("%d", &opcao);
        getchar(); // Limpar buffer

        switch(opcao) {
            case 1: criar_usuario(); break;
            case 2: listar_usuarios(); break;
            case 3: atualizar_usuario(); break;
            case 4: deletar_usuario(); break;
            case 0: printf("Saindo...\n"); break;
            default: printf("Opção inválida!\n");
        }
    } while(opcao != 0);

    return 0;
}

void criar_usuario() {
    FILE *file = fopen(DB_FILE, "ab");
    Usuario u;

    printf("ID: ");
    scanf("%d", &u.id);
    getchar();
    printf("Nome: ");
    fgets(u.nome, 50, stdin);
    u.nome[strcspn(u.nome, "\n")] = 0;
    printf("Email: ");
    fgets(u.email, 50, stdin);
    u.email[strcspn(u.email, "\n")] = 0;

    fwrite(&u, sizeof(Usuario), 1, file);
    fclose(file);
    printf("Usuário salvo com sucesso!\n");
}

void listar_usuarios() {
    FILE *file = fopen(DB_FILE, "rb");
    if (file == NULL) {
        printf("Banco de dados vazio ou inexistente.\n");
        return;
    }

    Usuario u;
    printf("\nID\tNome\t\tEmail\n");
    printf("--------------------------------------\n");
    while(fread(&u, sizeof(Usuario), 1, file)) {
        printf("%d\t%s\t\t%s\n", u.id, u.nome, u.email);
    }
    fclose(file);
}

void atualizar_usuario() {
    FILE *file = fopen(DB_FILE, "rb+");
    if (!file) return;

    int id, encontrado = 0;
    Usuario u;

    printf("Digite o ID para atualizar: ");
    scanf("%d", &id);

    while(fread(&u, sizeof(Usuario), 1, file)) {
        if(u.id == id) {
            printf("Novo Nome: ");
            getchar();
            fgets(u.nome, 50, stdin);
            u.nome[strcspn(u.nome, "\n")] = 0;
            
            // Volta o ponteiro do arquivo para sobrescrever o registro
            fseek(file, -sizeof(Usuario), SEEK_CUR);
            fwrite(&u, sizeof(Usuario), 1, file);
            encontrado = 1;
            break;
        }
    }
    if(!encontrado) printf("Usuário não encontrado.\n");
    fclose(file);
}

void deletar_usuario() {
    FILE *file = fopen(DB_FILE, "rb");
    FILE *temp = fopen("temp.dat", "wb");
    int id, encontrado = 0;
    Usuario u;

    printf("Digite o ID para deletar: ");
    scanf("%d", &id);

    while(fread(&u, sizeof(Usuario), 1, file)) {
        if(u.id != id) {
            fwrite(&u, sizeof(Usuario), 1, temp);
        } else {
            encontrado = 1;
        }
    }

    fclose(file);
    fclose(temp);

    remove(DB_FILE);
    rename("temp.dat", DB_FILE);

    if(encontrado) printf("Usuário removido!\n");
    else printf("ID não encontrado.\n");
}
