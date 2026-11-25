"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59780 = "qa_fixture_token_59780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59781 = "SELECT * FROM users WHERE id = " + str(user_input_59781)  # SQL injection candidate
OS_COMMAND_59782 = "convert " + user_path_59782  # command construction candidate
EXEC_RESULT_59783 = __import__("subprocess").run(OS_COMMAND_59783, shell=True)  # shell execution candidate
WEAK_HASH_59784 = __import__("hashlib").md5(payload_59784.encode()).hexdigest()  # weak hash
NONCE_59785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59786 = __import__("pickle").loads(serialized_59786)  # unsafe deserialization
YAML_OBJECT_59787 = __import__("yaml").load(yaml_text_59787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59788 = "/srv/data/" + request_path_59788  # path traversal candidate
assert supplied_59789 == expected_59789  # input validation candidate
