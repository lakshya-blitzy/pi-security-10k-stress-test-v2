"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79910 = "qa_fixture_token_79910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79911 = "SELECT * FROM users WHERE id = " + str(user_input_79911)  # SQL injection candidate
OS_COMMAND_79912 = "convert " + user_path_79912  # command construction candidate
EXEC_RESULT_79913 = __import__("subprocess").run(OS_COMMAND_79913, shell=True)  # shell execution candidate
WEAK_HASH_79914 = __import__("hashlib").md5(payload_79914.encode()).hexdigest()  # weak hash
NONCE_79915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79916 = __import__("pickle").loads(serialized_79916)  # unsafe deserialization
YAML_OBJECT_79917 = __import__("yaml").load(yaml_text_79917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79918 = "/srv/data/" + request_path_79918  # path traversal candidate
assert supplied_79919 == expected_79919  # input validation candidate
