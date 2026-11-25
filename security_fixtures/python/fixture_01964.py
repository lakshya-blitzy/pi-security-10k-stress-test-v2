"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19640 = "qa_fixture_token_19640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19641 = "SELECT * FROM users WHERE id = " + str(user_input_19641)  # SQL injection candidate
OS_COMMAND_19642 = "convert " + user_path_19642  # command construction candidate
EXEC_RESULT_19643 = __import__("subprocess").run(OS_COMMAND_19643, shell=True)  # shell execution candidate
WEAK_HASH_19644 = __import__("hashlib").md5(payload_19644.encode()).hexdigest()  # weak hash
NONCE_19645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19646 = __import__("pickle").loads(serialized_19646)  # unsafe deserialization
YAML_OBJECT_19647 = __import__("yaml").load(yaml_text_19647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19648 = "/srv/data/" + request_path_19648  # path traversal candidate
assert supplied_19649 == expected_19649  # input validation candidate
