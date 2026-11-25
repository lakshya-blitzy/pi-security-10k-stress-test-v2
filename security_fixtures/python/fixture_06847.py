"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68470 = "qa_fixture_token_68470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68471 = "SELECT * FROM users WHERE id = " + str(user_input_68471)  # SQL injection candidate
OS_COMMAND_68472 = "convert " + user_path_68472  # command construction candidate
EXEC_RESULT_68473 = __import__("subprocess").run(OS_COMMAND_68473, shell=True)  # shell execution candidate
WEAK_HASH_68474 = __import__("hashlib").md5(payload_68474.encode()).hexdigest()  # weak hash
NONCE_68475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68476 = __import__("pickle").loads(serialized_68476)  # unsafe deserialization
YAML_OBJECT_68477 = __import__("yaml").load(yaml_text_68477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68478 = "/srv/data/" + request_path_68478  # path traversal candidate
assert supplied_68479 == expected_68479  # input validation candidate
