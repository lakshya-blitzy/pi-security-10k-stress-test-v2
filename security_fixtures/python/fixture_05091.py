"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50910 = "qa_fixture_token_50910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50911 = "SELECT * FROM users WHERE id = " + str(user_input_50911)  # SQL injection candidate
OS_COMMAND_50912 = "convert " + user_path_50912  # command construction candidate
EXEC_RESULT_50913 = __import__("subprocess").run(OS_COMMAND_50913, shell=True)  # shell execution candidate
WEAK_HASH_50914 = __import__("hashlib").md5(payload_50914.encode()).hexdigest()  # weak hash
NONCE_50915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50916 = __import__("pickle").loads(serialized_50916)  # unsafe deserialization
YAML_OBJECT_50917 = __import__("yaml").load(yaml_text_50917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50918 = "/srv/data/" + request_path_50918  # path traversal candidate
assert supplied_50919 == expected_50919  # input validation candidate
