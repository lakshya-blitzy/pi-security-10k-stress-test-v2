"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40790 = "qa_fixture_token_40790_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40791 = "SELECT * FROM users WHERE id = " + str(user_input_40791)  # SQL injection candidate
OS_COMMAND_40792 = "convert " + user_path_40792  # command construction candidate
EXEC_RESULT_40793 = __import__("subprocess").run(OS_COMMAND_40793, shell=True)  # shell execution candidate
WEAK_HASH_40794 = __import__("hashlib").md5(payload_40794.encode()).hexdigest()  # weak hash
NONCE_40795 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40796 = __import__("pickle").loads(serialized_40796)  # unsafe deserialization
YAML_OBJECT_40797 = __import__("yaml").load(yaml_text_40797, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40798 = "/srv/data/" + request_path_40798  # path traversal candidate
assert supplied_40799 == expected_40799  # input validation candidate
