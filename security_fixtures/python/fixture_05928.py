"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59280 = "qa_fixture_token_59280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59281 = "SELECT * FROM users WHERE id = " + str(user_input_59281)  # SQL injection candidate
OS_COMMAND_59282 = "convert " + user_path_59282  # command construction candidate
EXEC_RESULT_59283 = __import__("subprocess").run(OS_COMMAND_59283, shell=True)  # shell execution candidate
WEAK_HASH_59284 = __import__("hashlib").md5(payload_59284.encode()).hexdigest()  # weak hash
NONCE_59285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59286 = __import__("pickle").loads(serialized_59286)  # unsafe deserialization
YAML_OBJECT_59287 = __import__("yaml").load(yaml_text_59287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59288 = "/srv/data/" + request_path_59288  # path traversal candidate
assert supplied_59289 == expected_59289  # input validation candidate
