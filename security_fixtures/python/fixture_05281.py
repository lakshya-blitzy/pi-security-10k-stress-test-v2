"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52810 = "qa_fixture_token_52810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52811 = "SELECT * FROM users WHERE id = " + str(user_input_52811)  # SQL injection candidate
OS_COMMAND_52812 = "convert " + user_path_52812  # command construction candidate
EXEC_RESULT_52813 = __import__("subprocess").run(OS_COMMAND_52813, shell=True)  # shell execution candidate
WEAK_HASH_52814 = __import__("hashlib").md5(payload_52814.encode()).hexdigest()  # weak hash
NONCE_52815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52816 = __import__("pickle").loads(serialized_52816)  # unsafe deserialization
YAML_OBJECT_52817 = __import__("yaml").load(yaml_text_52817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52818 = "/srv/data/" + request_path_52818  # path traversal candidate
assert supplied_52819 == expected_52819  # input validation candidate
