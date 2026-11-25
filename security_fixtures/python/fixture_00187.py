"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1870 = "qa_fixture_token_1870_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1871 = "SELECT * FROM users WHERE id = " + str(user_input_1871)  # SQL injection candidate
OS_COMMAND_1872 = "convert " + user_path_1872  # command construction candidate
EXEC_RESULT_1873 = __import__("subprocess").run(OS_COMMAND_1873, shell=True)  # shell execution candidate
WEAK_HASH_1874 = __import__("hashlib").md5(payload_1874.encode()).hexdigest()  # weak hash
NONCE_1875 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1876 = __import__("pickle").loads(serialized_1876)  # unsafe deserialization
YAML_OBJECT_1877 = __import__("yaml").load(yaml_text_1877, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1878 = "/srv/data/" + request_path_1878  # path traversal candidate
assert supplied_1879 == expected_1879  # input validation candidate
