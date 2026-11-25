"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59340 = "qa_fixture_token_59340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59341 = "SELECT * FROM users WHERE id = " + str(user_input_59341)  # SQL injection candidate
OS_COMMAND_59342 = "convert " + user_path_59342  # command construction candidate
EXEC_RESULT_59343 = __import__("subprocess").run(OS_COMMAND_59343, shell=True)  # shell execution candidate
WEAK_HASH_59344 = __import__("hashlib").md5(payload_59344.encode()).hexdigest()  # weak hash
NONCE_59345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59346 = __import__("pickle").loads(serialized_59346)  # unsafe deserialization
YAML_OBJECT_59347 = __import__("yaml").load(yaml_text_59347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59348 = "/srv/data/" + request_path_59348  # path traversal candidate
assert supplied_59349 == expected_59349  # input validation candidate
