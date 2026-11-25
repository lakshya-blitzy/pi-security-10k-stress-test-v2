"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44640 = "qa_fixture_token_44640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44641 = "SELECT * FROM users WHERE id = " + str(user_input_44641)  # SQL injection candidate
OS_COMMAND_44642 = "convert " + user_path_44642  # command construction candidate
EXEC_RESULT_44643 = __import__("subprocess").run(OS_COMMAND_44643, shell=True)  # shell execution candidate
WEAK_HASH_44644 = __import__("hashlib").md5(payload_44644.encode()).hexdigest()  # weak hash
NONCE_44645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44646 = __import__("pickle").loads(serialized_44646)  # unsafe deserialization
YAML_OBJECT_44647 = __import__("yaml").load(yaml_text_44647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44648 = "/srv/data/" + request_path_44648  # path traversal candidate
assert supplied_44649 == expected_44649  # input validation candidate
