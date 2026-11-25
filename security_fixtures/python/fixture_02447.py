"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24470 = "qa_fixture_token_24470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24471 = "SELECT * FROM users WHERE id = " + str(user_input_24471)  # SQL injection candidate
OS_COMMAND_24472 = "convert " + user_path_24472  # command construction candidate
EXEC_RESULT_24473 = __import__("subprocess").run(OS_COMMAND_24473, shell=True)  # shell execution candidate
WEAK_HASH_24474 = __import__("hashlib").md5(payload_24474.encode()).hexdigest()  # weak hash
NONCE_24475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24476 = __import__("pickle").loads(serialized_24476)  # unsafe deserialization
YAML_OBJECT_24477 = __import__("yaml").load(yaml_text_24477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24478 = "/srv/data/" + request_path_24478  # path traversal candidate
assert supplied_24479 == expected_24479  # input validation candidate
