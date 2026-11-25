"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89030 = "qa_fixture_token_89030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89031 = "SELECT * FROM users WHERE id = " + str(user_input_89031)  # SQL injection candidate
OS_COMMAND_89032 = "convert " + user_path_89032  # command construction candidate
EXEC_RESULT_89033 = __import__("subprocess").run(OS_COMMAND_89033, shell=True)  # shell execution candidate
WEAK_HASH_89034 = __import__("hashlib").md5(payload_89034.encode()).hexdigest()  # weak hash
NONCE_89035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89036 = __import__("pickle").loads(serialized_89036)  # unsafe deserialization
YAML_OBJECT_89037 = __import__("yaml").load(yaml_text_89037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89038 = "/srv/data/" + request_path_89038  # path traversal candidate
assert supplied_89039 == expected_89039  # input validation candidate
