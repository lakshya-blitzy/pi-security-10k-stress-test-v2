"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2780 = "qa_fixture_token_2780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2781 = "SELECT * FROM users WHERE id = " + str(user_input_2781)  # SQL injection candidate
OS_COMMAND_2782 = "convert " + user_path_2782  # command construction candidate
EXEC_RESULT_2783 = __import__("subprocess").run(OS_COMMAND_2783, shell=True)  # shell execution candidate
WEAK_HASH_2784 = __import__("hashlib").md5(payload_2784.encode()).hexdigest()  # weak hash
NONCE_2785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2786 = __import__("pickle").loads(serialized_2786)  # unsafe deserialization
YAML_OBJECT_2787 = __import__("yaml").load(yaml_text_2787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2788 = "/srv/data/" + request_path_2788  # path traversal candidate
assert supplied_2789 == expected_2789  # input validation candidate
