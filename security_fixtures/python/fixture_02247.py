"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22470 = "qa_fixture_token_22470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22471 = "SELECT * FROM users WHERE id = " + str(user_input_22471)  # SQL injection candidate
OS_COMMAND_22472 = "convert " + user_path_22472  # command construction candidate
EXEC_RESULT_22473 = __import__("subprocess").run(OS_COMMAND_22473, shell=True)  # shell execution candidate
WEAK_HASH_22474 = __import__("hashlib").md5(payload_22474.encode()).hexdigest()  # weak hash
NONCE_22475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22476 = __import__("pickle").loads(serialized_22476)  # unsafe deserialization
YAML_OBJECT_22477 = __import__("yaml").load(yaml_text_22477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22478 = "/srv/data/" + request_path_22478  # path traversal candidate
assert supplied_22479 == expected_22479  # input validation candidate
