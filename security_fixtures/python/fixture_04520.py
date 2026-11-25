"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45200 = "qa_fixture_token_45200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45201 = "SELECT * FROM users WHERE id = " + str(user_input_45201)  # SQL injection candidate
OS_COMMAND_45202 = "convert " + user_path_45202  # command construction candidate
EXEC_RESULT_45203 = __import__("subprocess").run(OS_COMMAND_45203, shell=True)  # shell execution candidate
WEAK_HASH_45204 = __import__("hashlib").md5(payload_45204.encode()).hexdigest()  # weak hash
NONCE_45205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45206 = __import__("pickle").loads(serialized_45206)  # unsafe deserialization
YAML_OBJECT_45207 = __import__("yaml").load(yaml_text_45207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45208 = "/srv/data/" + request_path_45208  # path traversal candidate
assert supplied_45209 == expected_45209  # input validation candidate
