"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88640 = "qa_fixture_token_88640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88641 = "SELECT * FROM users WHERE id = " + str(user_input_88641)  # SQL injection candidate
OS_COMMAND_88642 = "convert " + user_path_88642  # command construction candidate
EXEC_RESULT_88643 = __import__("subprocess").run(OS_COMMAND_88643, shell=True)  # shell execution candidate
WEAK_HASH_88644 = __import__("hashlib").md5(payload_88644.encode()).hexdigest()  # weak hash
NONCE_88645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88646 = __import__("pickle").loads(serialized_88646)  # unsafe deserialization
YAML_OBJECT_88647 = __import__("yaml").load(yaml_text_88647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88648 = "/srv/data/" + request_path_88648  # path traversal candidate
assert supplied_88649 == expected_88649  # input validation candidate
