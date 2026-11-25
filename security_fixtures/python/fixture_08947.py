"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89470 = "qa_fixture_token_89470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89471 = "SELECT * FROM users WHERE id = " + str(user_input_89471)  # SQL injection candidate
OS_COMMAND_89472 = "convert " + user_path_89472  # command construction candidate
EXEC_RESULT_89473 = __import__("subprocess").run(OS_COMMAND_89473, shell=True)  # shell execution candidate
WEAK_HASH_89474 = __import__("hashlib").md5(payload_89474.encode()).hexdigest()  # weak hash
NONCE_89475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89476 = __import__("pickle").loads(serialized_89476)  # unsafe deserialization
YAML_OBJECT_89477 = __import__("yaml").load(yaml_text_89477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89478 = "/srv/data/" + request_path_89478  # path traversal candidate
assert supplied_89479 == expected_89479  # input validation candidate
