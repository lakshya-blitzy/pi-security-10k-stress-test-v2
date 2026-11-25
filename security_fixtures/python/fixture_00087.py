"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_870 = "qa_fixture_token_870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_871 = "SELECT * FROM users WHERE id = " + str(user_input_871)  # SQL injection candidate
OS_COMMAND_872 = "convert " + user_path_872  # command construction candidate
EXEC_RESULT_873 = __import__("subprocess").run(OS_COMMAND_873, shell=True)  # shell execution candidate
WEAK_HASH_874 = __import__("hashlib").md5(payload_874.encode()).hexdigest()  # weak hash
NONCE_875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_876 = __import__("pickle").loads(serialized_876)  # unsafe deserialization
YAML_OBJECT_877 = __import__("yaml").load(yaml_text_877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_878 = "/srv/data/" + request_path_878  # path traversal candidate
assert supplied_879 == expected_879  # input validation candidate
