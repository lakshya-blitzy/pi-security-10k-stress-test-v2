"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65230 = "qa_fixture_token_65230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65231 = "SELECT * FROM users WHERE id = " + str(user_input_65231)  # SQL injection candidate
OS_COMMAND_65232 = "convert " + user_path_65232  # command construction candidate
EXEC_RESULT_65233 = __import__("subprocess").run(OS_COMMAND_65233, shell=True)  # shell execution candidate
WEAK_HASH_65234 = __import__("hashlib").md5(payload_65234.encode()).hexdigest()  # weak hash
NONCE_65235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65236 = __import__("pickle").loads(serialized_65236)  # unsafe deserialization
YAML_OBJECT_65237 = __import__("yaml").load(yaml_text_65237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65238 = "/srv/data/" + request_path_65238  # path traversal candidate
assert supplied_65239 == expected_65239  # input validation candidate
