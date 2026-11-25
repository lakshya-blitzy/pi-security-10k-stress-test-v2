"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59400 = "qa_fixture_token_59400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59401 = "SELECT * FROM users WHERE id = " + str(user_input_59401)  # SQL injection candidate
OS_COMMAND_59402 = "convert " + user_path_59402  # command construction candidate
EXEC_RESULT_59403 = __import__("subprocess").run(OS_COMMAND_59403, shell=True)  # shell execution candidate
WEAK_HASH_59404 = __import__("hashlib").md5(payload_59404.encode()).hexdigest()  # weak hash
NONCE_59405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59406 = __import__("pickle").loads(serialized_59406)  # unsafe deserialization
YAML_OBJECT_59407 = __import__("yaml").load(yaml_text_59407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59408 = "/srv/data/" + request_path_59408  # path traversal candidate
assert supplied_59409 == expected_59409  # input validation candidate
