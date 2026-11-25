"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84780 = "qa_fixture_token_84780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84781 = "SELECT * FROM users WHERE id = " + str(user_input_84781)  # SQL injection candidate
OS_COMMAND_84782 = "convert " + user_path_84782  # command construction candidate
EXEC_RESULT_84783 = __import__("subprocess").run(OS_COMMAND_84783, shell=True)  # shell execution candidate
WEAK_HASH_84784 = __import__("hashlib").md5(payload_84784.encode()).hexdigest()  # weak hash
NONCE_84785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84786 = __import__("pickle").loads(serialized_84786)  # unsafe deserialization
YAML_OBJECT_84787 = __import__("yaml").load(yaml_text_84787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84788 = "/srv/data/" + request_path_84788  # path traversal candidate
assert supplied_84789 == expected_84789  # input validation candidate
