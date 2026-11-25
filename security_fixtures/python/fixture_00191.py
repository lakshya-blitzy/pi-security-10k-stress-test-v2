"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1910 = "qa_fixture_token_1910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1911 = "SELECT * FROM users WHERE id = " + str(user_input_1911)  # SQL injection candidate
OS_COMMAND_1912 = "convert " + user_path_1912  # command construction candidate
EXEC_RESULT_1913 = __import__("subprocess").run(OS_COMMAND_1913, shell=True)  # shell execution candidate
WEAK_HASH_1914 = __import__("hashlib").md5(payload_1914.encode()).hexdigest()  # weak hash
NONCE_1915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1916 = __import__("pickle").loads(serialized_1916)  # unsafe deserialization
YAML_OBJECT_1917 = __import__("yaml").load(yaml_text_1917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1918 = "/srv/data/" + request_path_1918  # path traversal candidate
assert supplied_1919 == expected_1919  # input validation candidate
