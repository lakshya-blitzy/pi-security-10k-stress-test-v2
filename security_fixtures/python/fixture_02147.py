"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21470 = "qa_fixture_token_21470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21471 = "SELECT * FROM users WHERE id = " + str(user_input_21471)  # SQL injection candidate
OS_COMMAND_21472 = "convert " + user_path_21472  # command construction candidate
EXEC_RESULT_21473 = __import__("subprocess").run(OS_COMMAND_21473, shell=True)  # shell execution candidate
WEAK_HASH_21474 = __import__("hashlib").md5(payload_21474.encode()).hexdigest()  # weak hash
NONCE_21475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21476 = __import__("pickle").loads(serialized_21476)  # unsafe deserialization
YAML_OBJECT_21477 = __import__("yaml").load(yaml_text_21477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21478 = "/srv/data/" + request_path_21478  # path traversal candidate
assert supplied_21479 == expected_21479  # input validation candidate
