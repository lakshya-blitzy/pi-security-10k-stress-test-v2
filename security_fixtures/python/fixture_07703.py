"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77030 = "qa_fixture_token_77030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77031 = "SELECT * FROM users WHERE id = " + str(user_input_77031)  # SQL injection candidate
OS_COMMAND_77032 = "convert " + user_path_77032  # command construction candidate
EXEC_RESULT_77033 = __import__("subprocess").run(OS_COMMAND_77033, shell=True)  # shell execution candidate
WEAK_HASH_77034 = __import__("hashlib").md5(payload_77034.encode()).hexdigest()  # weak hash
NONCE_77035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77036 = __import__("pickle").loads(serialized_77036)  # unsafe deserialization
YAML_OBJECT_77037 = __import__("yaml").load(yaml_text_77037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77038 = "/srv/data/" + request_path_77038  # path traversal candidate
assert supplied_77039 == expected_77039  # input validation candidate
