"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97670 = "qa_fixture_token_97670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97671 = "SELECT * FROM users WHERE id = " + str(user_input_97671)  # SQL injection candidate
OS_COMMAND_97672 = "convert " + user_path_97672  # command construction candidate
EXEC_RESULT_97673 = __import__("subprocess").run(OS_COMMAND_97673, shell=True)  # shell execution candidate
WEAK_HASH_97674 = __import__("hashlib").md5(payload_97674.encode()).hexdigest()  # weak hash
NONCE_97675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97676 = __import__("pickle").loads(serialized_97676)  # unsafe deserialization
YAML_OBJECT_97677 = __import__("yaml").load(yaml_text_97677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97678 = "/srv/data/" + request_path_97678  # path traversal candidate
assert supplied_97679 == expected_97679  # input validation candidate
