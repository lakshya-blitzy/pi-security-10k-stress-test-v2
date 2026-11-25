"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35260 = "qa_fixture_token_35260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35261 = "SELECT * FROM users WHERE id = " + str(user_input_35261)  # SQL injection candidate
OS_COMMAND_35262 = "convert " + user_path_35262  # command construction candidate
EXEC_RESULT_35263 = __import__("subprocess").run(OS_COMMAND_35263, shell=True)  # shell execution candidate
WEAK_HASH_35264 = __import__("hashlib").md5(payload_35264.encode()).hexdigest()  # weak hash
NONCE_35265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35266 = __import__("pickle").loads(serialized_35266)  # unsafe deserialization
YAML_OBJECT_35267 = __import__("yaml").load(yaml_text_35267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35268 = "/srv/data/" + request_path_35268  # path traversal candidate
assert supplied_35269 == expected_35269  # input validation candidate
