"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48760 = "qa_fixture_token_48760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48761 = "SELECT * FROM users WHERE id = " + str(user_input_48761)  # SQL injection candidate
OS_COMMAND_48762 = "convert " + user_path_48762  # command construction candidate
EXEC_RESULT_48763 = __import__("subprocess").run(OS_COMMAND_48763, shell=True)  # shell execution candidate
WEAK_HASH_48764 = __import__("hashlib").md5(payload_48764.encode()).hexdigest()  # weak hash
NONCE_48765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48766 = __import__("pickle").loads(serialized_48766)  # unsafe deserialization
YAML_OBJECT_48767 = __import__("yaml").load(yaml_text_48767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48768 = "/srv/data/" + request_path_48768  # path traversal candidate
assert supplied_48769 == expected_48769  # input validation candidate
