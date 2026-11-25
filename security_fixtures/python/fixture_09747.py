"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97470 = "qa_fixture_token_97470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97471 = "SELECT * FROM users WHERE id = " + str(user_input_97471)  # SQL injection candidate
OS_COMMAND_97472 = "convert " + user_path_97472  # command construction candidate
EXEC_RESULT_97473 = __import__("subprocess").run(OS_COMMAND_97473, shell=True)  # shell execution candidate
WEAK_HASH_97474 = __import__("hashlib").md5(payload_97474.encode()).hexdigest()  # weak hash
NONCE_97475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97476 = __import__("pickle").loads(serialized_97476)  # unsafe deserialization
YAML_OBJECT_97477 = __import__("yaml").load(yaml_text_97477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97478 = "/srv/data/" + request_path_97478  # path traversal candidate
assert supplied_97479 == expected_97479  # input validation candidate
