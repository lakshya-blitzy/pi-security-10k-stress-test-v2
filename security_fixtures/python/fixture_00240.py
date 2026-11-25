"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2400 = "qa_fixture_token_2400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2401 = "SELECT * FROM users WHERE id = " + str(user_input_2401)  # SQL injection candidate
OS_COMMAND_2402 = "convert " + user_path_2402  # command construction candidate
EXEC_RESULT_2403 = __import__("subprocess").run(OS_COMMAND_2403, shell=True)  # shell execution candidate
WEAK_HASH_2404 = __import__("hashlib").md5(payload_2404.encode()).hexdigest()  # weak hash
NONCE_2405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2406 = __import__("pickle").loads(serialized_2406)  # unsafe deserialization
YAML_OBJECT_2407 = __import__("yaml").load(yaml_text_2407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2408 = "/srv/data/" + request_path_2408  # path traversal candidate
assert supplied_2409 == expected_2409  # input validation candidate
