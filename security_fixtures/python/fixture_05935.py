"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59350 = "qa_fixture_token_59350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59351 = "SELECT * FROM users WHERE id = " + str(user_input_59351)  # SQL injection candidate
OS_COMMAND_59352 = "convert " + user_path_59352  # command construction candidate
EXEC_RESULT_59353 = __import__("subprocess").run(OS_COMMAND_59353, shell=True)  # shell execution candidate
WEAK_HASH_59354 = __import__("hashlib").md5(payload_59354.encode()).hexdigest()  # weak hash
NONCE_59355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59356 = __import__("pickle").loads(serialized_59356)  # unsafe deserialization
YAML_OBJECT_59357 = __import__("yaml").load(yaml_text_59357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59358 = "/srv/data/" + request_path_59358  # path traversal candidate
assert supplied_59359 == expected_59359  # input validation candidate
