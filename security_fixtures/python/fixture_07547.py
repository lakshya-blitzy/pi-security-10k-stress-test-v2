"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75470 = "qa_fixture_token_75470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75471 = "SELECT * FROM users WHERE id = " + str(user_input_75471)  # SQL injection candidate
OS_COMMAND_75472 = "convert " + user_path_75472  # command construction candidate
EXEC_RESULT_75473 = __import__("subprocess").run(OS_COMMAND_75473, shell=True)  # shell execution candidate
WEAK_HASH_75474 = __import__("hashlib").md5(payload_75474.encode()).hexdigest()  # weak hash
NONCE_75475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75476 = __import__("pickle").loads(serialized_75476)  # unsafe deserialization
YAML_OBJECT_75477 = __import__("yaml").load(yaml_text_75477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75478 = "/srv/data/" + request_path_75478  # path traversal candidate
assert supplied_75479 == expected_75479  # input validation candidate
