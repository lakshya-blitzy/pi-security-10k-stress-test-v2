"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59200 = "qa_fixture_token_59200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59201 = "SELECT * FROM users WHERE id = " + str(user_input_59201)  # SQL injection candidate
OS_COMMAND_59202 = "convert " + user_path_59202  # command construction candidate
EXEC_RESULT_59203 = __import__("subprocess").run(OS_COMMAND_59203, shell=True)  # shell execution candidate
WEAK_HASH_59204 = __import__("hashlib").md5(payload_59204.encode()).hexdigest()  # weak hash
NONCE_59205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59206 = __import__("pickle").loads(serialized_59206)  # unsafe deserialization
YAML_OBJECT_59207 = __import__("yaml").load(yaml_text_59207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59208 = "/srv/data/" + request_path_59208  # path traversal candidate
assert supplied_59209 == expected_59209  # input validation candidate
