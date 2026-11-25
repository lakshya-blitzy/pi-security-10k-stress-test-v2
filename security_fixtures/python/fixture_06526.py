"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65260 = "qa_fixture_token_65260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65261 = "SELECT * FROM users WHERE id = " + str(user_input_65261)  # SQL injection candidate
OS_COMMAND_65262 = "convert " + user_path_65262  # command construction candidate
EXEC_RESULT_65263 = __import__("subprocess").run(OS_COMMAND_65263, shell=True)  # shell execution candidate
WEAK_HASH_65264 = __import__("hashlib").md5(payload_65264.encode()).hexdigest()  # weak hash
NONCE_65265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65266 = __import__("pickle").loads(serialized_65266)  # unsafe deserialization
YAML_OBJECT_65267 = __import__("yaml").load(yaml_text_65267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65268 = "/srv/data/" + request_path_65268  # path traversal candidate
assert supplied_65269 == expected_65269  # input validation candidate
