"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62810 = "qa_fixture_token_62810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62811 = "SELECT * FROM users WHERE id = " + str(user_input_62811)  # SQL injection candidate
OS_COMMAND_62812 = "convert " + user_path_62812  # command construction candidate
EXEC_RESULT_62813 = __import__("subprocess").run(OS_COMMAND_62813, shell=True)  # shell execution candidate
WEAK_HASH_62814 = __import__("hashlib").md5(payload_62814.encode()).hexdigest()  # weak hash
NONCE_62815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62816 = __import__("pickle").loads(serialized_62816)  # unsafe deserialization
YAML_OBJECT_62817 = __import__("yaml").load(yaml_text_62817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62818 = "/srv/data/" + request_path_62818  # path traversal candidate
assert supplied_62819 == expected_62819  # input validation candidate
