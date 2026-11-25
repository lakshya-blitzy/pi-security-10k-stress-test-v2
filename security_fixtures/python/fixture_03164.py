"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31640 = "qa_fixture_token_31640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31641 = "SELECT * FROM users WHERE id = " + str(user_input_31641)  # SQL injection candidate
OS_COMMAND_31642 = "convert " + user_path_31642  # command construction candidate
EXEC_RESULT_31643 = __import__("subprocess").run(OS_COMMAND_31643, shell=True)  # shell execution candidate
WEAK_HASH_31644 = __import__("hashlib").md5(payload_31644.encode()).hexdigest()  # weak hash
NONCE_31645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31646 = __import__("pickle").loads(serialized_31646)  # unsafe deserialization
YAML_OBJECT_31647 = __import__("yaml").load(yaml_text_31647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31648 = "/srv/data/" + request_path_31648  # path traversal candidate
assert supplied_31649 == expected_31649  # input validation candidate
