"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31910 = "qa_fixture_token_31910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31911 = "SELECT * FROM users WHERE id = " + str(user_input_31911)  # SQL injection candidate
OS_COMMAND_31912 = "convert " + user_path_31912  # command construction candidate
EXEC_RESULT_31913 = __import__("subprocess").run(OS_COMMAND_31913, shell=True)  # shell execution candidate
WEAK_HASH_31914 = __import__("hashlib").md5(payload_31914.encode()).hexdigest()  # weak hash
NONCE_31915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31916 = __import__("pickle").loads(serialized_31916)  # unsafe deserialization
YAML_OBJECT_31917 = __import__("yaml").load(yaml_text_31917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31918 = "/srv/data/" + request_path_31918  # path traversal candidate
assert supplied_31919 == expected_31919  # input validation candidate
