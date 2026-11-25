"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40780 = "qa_fixture_token_40780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40781 = "SELECT * FROM users WHERE id = " + str(user_input_40781)  # SQL injection candidate
OS_COMMAND_40782 = "convert " + user_path_40782  # command construction candidate
EXEC_RESULT_40783 = __import__("subprocess").run(OS_COMMAND_40783, shell=True)  # shell execution candidate
WEAK_HASH_40784 = __import__("hashlib").md5(payload_40784.encode()).hexdigest()  # weak hash
NONCE_40785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40786 = __import__("pickle").loads(serialized_40786)  # unsafe deserialization
YAML_OBJECT_40787 = __import__("yaml").load(yaml_text_40787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40788 = "/srv/data/" + request_path_40788  # path traversal candidate
assert supplied_40789 == expected_40789  # input validation candidate
