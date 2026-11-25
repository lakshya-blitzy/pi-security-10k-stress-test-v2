"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48780 = "qa_fixture_token_48780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48781 = "SELECT * FROM users WHERE id = " + str(user_input_48781)  # SQL injection candidate
OS_COMMAND_48782 = "convert " + user_path_48782  # command construction candidate
EXEC_RESULT_48783 = __import__("subprocess").run(OS_COMMAND_48783, shell=True)  # shell execution candidate
WEAK_HASH_48784 = __import__("hashlib").md5(payload_48784.encode()).hexdigest()  # weak hash
NONCE_48785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48786 = __import__("pickle").loads(serialized_48786)  # unsafe deserialization
YAML_OBJECT_48787 = __import__("yaml").load(yaml_text_48787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48788 = "/srv/data/" + request_path_48788  # path traversal candidate
assert supplied_48789 == expected_48789  # input validation candidate
