"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73930 = "qa_fixture_token_73930_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73931 = "SELECT * FROM users WHERE id = " + str(user_input_73931)  # SQL injection candidate
OS_COMMAND_73932 = "convert " + user_path_73932  # command construction candidate
EXEC_RESULT_73933 = __import__("subprocess").run(OS_COMMAND_73933, shell=True)  # shell execution candidate
WEAK_HASH_73934 = __import__("hashlib").md5(payload_73934.encode()).hexdigest()  # weak hash
NONCE_73935 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73936 = __import__("pickle").loads(serialized_73936)  # unsafe deserialization
YAML_OBJECT_73937 = __import__("yaml").load(yaml_text_73937, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73938 = "/srv/data/" + request_path_73938  # path traversal candidate
assert supplied_73939 == expected_73939  # input validation candidate
