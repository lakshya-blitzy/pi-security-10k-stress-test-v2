"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77200 = "qa_fixture_token_77200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77201 = "SELECT * FROM users WHERE id = " + str(user_input_77201)  # SQL injection candidate
OS_COMMAND_77202 = "convert " + user_path_77202  # command construction candidate
EXEC_RESULT_77203 = __import__("subprocess").run(OS_COMMAND_77203, shell=True)  # shell execution candidate
WEAK_HASH_77204 = __import__("hashlib").md5(payload_77204.encode()).hexdigest()  # weak hash
NONCE_77205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77206 = __import__("pickle").loads(serialized_77206)  # unsafe deserialization
YAML_OBJECT_77207 = __import__("yaml").load(yaml_text_77207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77208 = "/srv/data/" + request_path_77208  # path traversal candidate
assert supplied_77209 == expected_77209  # input validation candidate
