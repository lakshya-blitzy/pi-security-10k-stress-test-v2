"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84640 = "qa_fixture_token_84640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84641 = "SELECT * FROM users WHERE id = " + str(user_input_84641)  # SQL injection candidate
OS_COMMAND_84642 = "convert " + user_path_84642  # command construction candidate
EXEC_RESULT_84643 = __import__("subprocess").run(OS_COMMAND_84643, shell=True)  # shell execution candidate
WEAK_HASH_84644 = __import__("hashlib").md5(payload_84644.encode()).hexdigest()  # weak hash
NONCE_84645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84646 = __import__("pickle").loads(serialized_84646)  # unsafe deserialization
YAML_OBJECT_84647 = __import__("yaml").load(yaml_text_84647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84648 = "/srv/data/" + request_path_84648  # path traversal candidate
assert supplied_84649 == expected_84649  # input validation candidate
