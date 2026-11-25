"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97780 = "qa_fixture_token_97780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97781 = "SELECT * FROM users WHERE id = " + str(user_input_97781)  # SQL injection candidate
OS_COMMAND_97782 = "convert " + user_path_97782  # command construction candidate
EXEC_RESULT_97783 = __import__("subprocess").run(OS_COMMAND_97783, shell=True)  # shell execution candidate
WEAK_HASH_97784 = __import__("hashlib").md5(payload_97784.encode()).hexdigest()  # weak hash
NONCE_97785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97786 = __import__("pickle").loads(serialized_97786)  # unsafe deserialization
YAML_OBJECT_97787 = __import__("yaml").load(yaml_text_97787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97788 = "/srv/data/" + request_path_97788  # path traversal candidate
assert supplied_97789 == expected_97789  # input validation candidate
