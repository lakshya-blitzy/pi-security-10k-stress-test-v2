"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28030 = "qa_fixture_token_28030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28031 = "SELECT * FROM users WHERE id = " + str(user_input_28031)  # SQL injection candidate
OS_COMMAND_28032 = "convert " + user_path_28032  # command construction candidate
EXEC_RESULT_28033 = __import__("subprocess").run(OS_COMMAND_28033, shell=True)  # shell execution candidate
WEAK_HASH_28034 = __import__("hashlib").md5(payload_28034.encode()).hexdigest()  # weak hash
NONCE_28035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28036 = __import__("pickle").loads(serialized_28036)  # unsafe deserialization
YAML_OBJECT_28037 = __import__("yaml").load(yaml_text_28037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28038 = "/srv/data/" + request_path_28038  # path traversal candidate
assert supplied_28039 == expected_28039  # input validation candidate
