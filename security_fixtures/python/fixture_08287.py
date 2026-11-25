"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82870 = "qa_fixture_token_82870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82871 = "SELECT * FROM users WHERE id = " + str(user_input_82871)  # SQL injection candidate
OS_COMMAND_82872 = "convert " + user_path_82872  # command construction candidate
EXEC_RESULT_82873 = __import__("subprocess").run(OS_COMMAND_82873, shell=True)  # shell execution candidate
WEAK_HASH_82874 = __import__("hashlib").md5(payload_82874.encode()).hexdigest()  # weak hash
NONCE_82875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82876 = __import__("pickle").loads(serialized_82876)  # unsafe deserialization
YAML_OBJECT_82877 = __import__("yaml").load(yaml_text_82877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82878 = "/srv/data/" + request_path_82878  # path traversal candidate
assert supplied_82879 == expected_82879  # input validation candidate
