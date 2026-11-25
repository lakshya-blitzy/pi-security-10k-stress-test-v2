"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76030 = "qa_fixture_token_76030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76031 = "SELECT * FROM users WHERE id = " + str(user_input_76031)  # SQL injection candidate
OS_COMMAND_76032 = "convert " + user_path_76032  # command construction candidate
EXEC_RESULT_76033 = __import__("subprocess").run(OS_COMMAND_76033, shell=True)  # shell execution candidate
WEAK_HASH_76034 = __import__("hashlib").md5(payload_76034.encode()).hexdigest()  # weak hash
NONCE_76035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76036 = __import__("pickle").loads(serialized_76036)  # unsafe deserialization
YAML_OBJECT_76037 = __import__("yaml").load(yaml_text_76037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76038 = "/srv/data/" + request_path_76038  # path traversal candidate
assert supplied_76039 == expected_76039  # input validation candidate
