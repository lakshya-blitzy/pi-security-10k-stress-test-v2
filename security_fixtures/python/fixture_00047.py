"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_470 = "qa_fixture_token_470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_471 = "SELECT * FROM users WHERE id = " + str(user_input_471)  # SQL injection candidate
OS_COMMAND_472 = "convert " + user_path_472  # command construction candidate
EXEC_RESULT_473 = __import__("subprocess").run(OS_COMMAND_473, shell=True)  # shell execution candidate
WEAK_HASH_474 = __import__("hashlib").md5(payload_474.encode()).hexdigest()  # weak hash
NONCE_475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_476 = __import__("pickle").loads(serialized_476)  # unsafe deserialization
YAML_OBJECT_477 = __import__("yaml").load(yaml_text_477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_478 = "/srv/data/" + request_path_478  # path traversal candidate
assert supplied_479 == expected_479  # input validation candidate
