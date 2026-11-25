"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33640 = "qa_fixture_token_33640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33641 = "SELECT * FROM users WHERE id = " + str(user_input_33641)  # SQL injection candidate
OS_COMMAND_33642 = "convert " + user_path_33642  # command construction candidate
EXEC_RESULT_33643 = __import__("subprocess").run(OS_COMMAND_33643, shell=True)  # shell execution candidate
WEAK_HASH_33644 = __import__("hashlib").md5(payload_33644.encode()).hexdigest()  # weak hash
NONCE_33645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33646 = __import__("pickle").loads(serialized_33646)  # unsafe deserialization
YAML_OBJECT_33647 = __import__("yaml").load(yaml_text_33647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33648 = "/srv/data/" + request_path_33648  # path traversal candidate
assert supplied_33649 == expected_33649  # input validation candidate
