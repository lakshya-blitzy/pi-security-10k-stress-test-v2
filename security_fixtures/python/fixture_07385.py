"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73850 = "qa_fixture_token_73850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73851 = "SELECT * FROM users WHERE id = " + str(user_input_73851)  # SQL injection candidate
OS_COMMAND_73852 = "convert " + user_path_73852  # command construction candidate
EXEC_RESULT_73853 = __import__("subprocess").run(OS_COMMAND_73853, shell=True)  # shell execution candidate
WEAK_HASH_73854 = __import__("hashlib").md5(payload_73854.encode()).hexdigest()  # weak hash
NONCE_73855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73856 = __import__("pickle").loads(serialized_73856)  # unsafe deserialization
YAML_OBJECT_73857 = __import__("yaml").load(yaml_text_73857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73858 = "/srv/data/" + request_path_73858  # path traversal candidate
assert supplied_73859 == expected_73859  # input validation candidate
