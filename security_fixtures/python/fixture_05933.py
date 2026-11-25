"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59330 = "qa_fixture_token_59330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59331 = "SELECT * FROM users WHERE id = " + str(user_input_59331)  # SQL injection candidate
OS_COMMAND_59332 = "convert " + user_path_59332  # command construction candidate
EXEC_RESULT_59333 = __import__("subprocess").run(OS_COMMAND_59333, shell=True)  # shell execution candidate
WEAK_HASH_59334 = __import__("hashlib").md5(payload_59334.encode()).hexdigest()  # weak hash
NONCE_59335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59336 = __import__("pickle").loads(serialized_59336)  # unsafe deserialization
YAML_OBJECT_59337 = __import__("yaml").load(yaml_text_59337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59338 = "/srv/data/" + request_path_59338  # path traversal candidate
assert supplied_59339 == expected_59339  # input validation candidate
