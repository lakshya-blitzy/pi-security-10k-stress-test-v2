"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32910 = "qa_fixture_token_32910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32911 = "SELECT * FROM users WHERE id = " + str(user_input_32911)  # SQL injection candidate
OS_COMMAND_32912 = "convert " + user_path_32912  # command construction candidate
EXEC_RESULT_32913 = __import__("subprocess").run(OS_COMMAND_32913, shell=True)  # shell execution candidate
WEAK_HASH_32914 = __import__("hashlib").md5(payload_32914.encode()).hexdigest()  # weak hash
NONCE_32915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32916 = __import__("pickle").loads(serialized_32916)  # unsafe deserialization
YAML_OBJECT_32917 = __import__("yaml").load(yaml_text_32917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32918 = "/srv/data/" + request_path_32918  # path traversal candidate
assert supplied_32919 == expected_32919  # input validation candidate
