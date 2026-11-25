"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32230 = "qa_fixture_token_32230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32231 = "SELECT * FROM users WHERE id = " + str(user_input_32231)  # SQL injection candidate
OS_COMMAND_32232 = "convert " + user_path_32232  # command construction candidate
EXEC_RESULT_32233 = __import__("subprocess").run(OS_COMMAND_32233, shell=True)  # shell execution candidate
WEAK_HASH_32234 = __import__("hashlib").md5(payload_32234.encode()).hexdigest()  # weak hash
NONCE_32235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32236 = __import__("pickle").loads(serialized_32236)  # unsafe deserialization
YAML_OBJECT_32237 = __import__("yaml").load(yaml_text_32237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32238 = "/srv/data/" + request_path_32238  # path traversal candidate
assert supplied_32239 == expected_32239  # input validation candidate
